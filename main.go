package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/mux"
	_ "github.com/mattn/go-sqlite3"
)

type Course struct {
	Course_id int    `json: "course_id"`
	Name      string `json: "name"`
	Sks       int    `json: "sks"`
	Term      int    `json: "term"`
	Jam_start string `json: "jam_start"`
	Jam_end   string `json: "jam_end"`
	Hari      string `json: "hari"`
}

type MyCourse struct {
	Mycourse_id int    `json: "mycourse_id"`
	Course_id   int    `json: "course_id"`
	Name        string `json: "name"`
	Sks         int    `json: "sks"`
	Term        int    `json: "term"`
	Jam_start   string `json: "jam_start"`
	Jam_end     string `json: "jam_end"`
	Hari        string `json: "hari"`
}

func main() {
	handleRequests()
}

func home(w http.ResponseWriter, r *http.Request) {

	db, err := sql.Open("sqlite3", "./course.db")

	if err != nil {
		log.Fatal(err)
	}

	//rows, err := db.Query("SELECT * FROM pertemuan")
	rows, err := db.Query("SELECT course.id AS course_id, course.name AS name, course.sks AS sks, course.term AS term, time(pertemuan.jam_start) AS jam_start, time(pertemuan.jam_end) AS jam_end, harienum.hari AS hari FROM course INNER JOIN pertemuan ON course.pertemuan_id = pertemuan.id INNER JOIN harienum ON harienum.id = pertemuan.hari ORDER BY term")
	if err != nil {
		log.Fatal(err)
	}

	Courses := []Course{}
	for rows.Next() {

		var c Course
		err = rows.Scan(&c.Course_id, &c.Name, &c.Sks, &c.Term, &c.Jam_start, &c.Jam_end, &c.Hari)
		if err != nil {
			log.Fatal(err)
		}
		Courses = append(Courses, c)
	}

	//fmt.Fprintf(w, Courses)
	fmt.Println("Home")

	json.NewEncoder(w).Encode(Courses)

}

// Nambah matkul
func addCourse(w http.ResponseWriter, r *http.Request) {
	decoder := json.NewDecoder(r.Body)
	type test_struct struct {
		Name string
	}
	var name test_struct
	err := decoder.Decode(&name)
	if err != nil {
		log.Fatal(err)
	}

	db, err := sql.Open("sqlite3", "./course.db")

	if err != nil {
		log.Fatal(err)
	}

	var id int
	test, err := db.Query("SELECT id FROM course WHERE name=$1", name.Name)

	if err != nil {
		log.Fatal(err)
	}

	for test.Next() {
		err = test.Scan(&id)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(id)
	}

	var hari string
	var jam string
	var hariada string
	var jamada string

	cekhari, err := db.Query("SELECT harienum.hari FROM course INNER JOIN pertemuan ON course.pertemuan_id = pertemuan.id INNER JOIN harienum ON harienum.id = pertemuan.hari WHERE course.id=$1", id)
	if err != nil {
		log.Fatal(err)
	}
	cekjam, err := db.Query("SELECT pertemuan.jam_start FROM course INNER JOIN pertemuan ON course.pertemuan_id = pertemuan.id INNER JOIN harienum ON harienum.id = pertemuan.hari WHERE course.id=$1", id)
	if err != nil {
		log.Fatal(err)
	}
	for cekhari.Next() {
		if err := cekhari.Scan(&hari); err != nil {
			log.Fatal(err)
		}
	}

	for cekjam.Next() {
		if err := cekjam.Scan(&jam); err != nil {
			log.Fatal(err)
		}
	}

	adahari, err := db.Query("SELECT harienum.hari FROM mycourse INNER JOIN course ON course.id = mycourse.course_id INNER JOIN pertemuan ON pertemuan.id = course.pertemuan_id INNER JOIN harienum ON harienum.id = pertemuan.hari WHERE harienum.hari=$1", hari)
	if err != nil {
		log.Fatal(err)
	}
	adajam, err := db.Query("SELECT pertemuan.jam_start FROM mycourse INNER JOIN course ON course.id = mycourse.course_id INNER JOIN pertemuan ON pertemuan.id = course.pertemuan_id INNER JOIN harienum ON harienum.id = pertemuan.hari WHERE pertemuan.jam_start=$1", jam)
	if err != nil {
		log.Fatal(err)
	}

	for adahari.Next() {
		if err := adahari.Scan(&hariada); err != nil {
			log.Fatal(err)
		}
	}

	for adajam.Next() {
		if err := adajam.Scan(&jamada); err != nil {
			log.Fatal(err)
		}
	}

	if hari == hariada && jam == jamada {
		w.WriteHeader(http.StatusInternalServerError)
		w.Write([]byte("500 - Something bad happened!"))
	}

	_, err = db.Exec("INSERT INTO mycourse(course_id) VALUES($1)", id)
	//_, err = db.Exec("INSERT INTO mycourse(course_id) VALUES(1)")
	if err != nil {
		log.Fatal(err)
	}

}

func getMyCourse(w http.ResponseWriter, r *http.Request) {
	db, err := sql.Open("sqlite3", "./course.db")

	if err != nil {
		log.Fatal(err)
	}

	rows, err := db.Query("SELECT mycourse.id, mycourse.course_id AS course_id, course.name AS name, course.sks AS sks, course.term AS term, time(pertemuan.jam_start) AS jam_start, time(pertemuan.jam_end) AS jam_end, harienum.hari AS hari FROM mycourse INNER JOIN course ON course.id = mycourse.course_id INNER JOIN pertemuan ON pertemuan.id = course.pertemuan_id INNER JOIN harienum ON harienum.id = pertemuan.hari ORDER BY term")

	if err != nil {
		log.Fatal(err)
	}

	Mycourse := []MyCourse{}

	for rows.Next() {
		var mc MyCourse
		err := rows.Scan(&mc.Mycourse_id, &mc.Course_id, &mc.Name, &mc.Sks, &mc.Term, &mc.Jam_start, &mc.Jam_end, &mc.Hari)
		if err != nil {
			log.Fatal(err)
		}

		Mycourse = append(Mycourse, mc)

	}
	fmt.Println(len(Mycourse))
	json.NewEncoder(w).Encode(Mycourse)
}

func handleRequests() {
	r := mux.NewRouter().StrictSlash(true)
	r.HandleFunc("/", home)
	r.HandleFunc("/pilih", addCourse).Methods("POST")
	r.HandleFunc("/mycourse", getMyCourse)
	log.Fatal(http.ListenAndServe(":8080", r))
}

/*

curl -X POST -H "Content-Type: application/json" \
    -d '{"name": "Despro"}' \
    http://localhost:8080/pilih
*/
