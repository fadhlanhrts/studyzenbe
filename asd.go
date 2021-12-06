package main

import (
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
