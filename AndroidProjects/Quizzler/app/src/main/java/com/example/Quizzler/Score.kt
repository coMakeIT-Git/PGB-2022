package com.example.Quizzler

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView

class Score : AppCompatActivity() {

    lateinit var    scorecard : TextView
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_score)

        scorecard = findViewById (R.id.scorecard)

        scorecard.text = intent.getIntExtra("score", 0).toString()



    }
}