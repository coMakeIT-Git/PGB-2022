package com.example.quizzler

//{
//    "response_code":0,
//    "results":[
//    {
//        "category":"Science: Computers",
//        "type":"multiple",
//        "difficulty":"easy",
//        "question":"What does the &quot;MP&quot; stand for in MP3?",
//        "correct_answer":"Moving Picture",
//        "incorrect_answers":[
//        "Music Player",
//        "Multi Pass",
//        "Micro Point"
//        ]
//    }


data class Result (val category:String, val type : String , val difficulty : String ,val question :String ,

                     val correct_answer :String , val incorrect_answers : List<String>)


data class QList(
    val response_code: Int,
    val results: List<Result>,

)