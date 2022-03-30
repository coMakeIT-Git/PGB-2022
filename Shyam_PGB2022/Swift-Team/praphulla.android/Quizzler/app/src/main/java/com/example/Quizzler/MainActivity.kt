package com.example.Quizzler
import android.content.Intent
import android.graphics.Color
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.ProgressBar
import android.os.Handler
import android.os.Looper
import android.widget.TextView
import com.example.quizzler.QList

class MainActivity : AppCompatActivity() {

    //declare global variables as lateinit to avoid compilation error
    lateinit  var Qdata : QList
    lateinit var QTV : TextView
    lateinit var Sbut : Button
    lateinit var O1but : Button
    lateinit var O2but : Button
    lateinit var O3but : Button
    lateinit var O4but : Button
    lateinit var pb : ProgressBar
    val i=0
    val mainHandler = Handler(Looper.getMainLooper()).post {
        System.out.println("Thread : " + Thread.currentThread().name)
    }




    var flag = false
    var canspos : Int = 0
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        Qdata =  QDataSingleton.Companion.QData // a common data source for entire app //access

        val currentquestion = intent.getIntExtra("currentQuestion", 0)







        QTV = findViewById(R.id.questionTV)
        Sbut = findViewById(R.id.butSubmit)
        O1but = findViewById(R.id.butOption1)
        O2but = findViewById(R.id.butOption2)
        O3but = findViewById(R.id.butOption3)
        O4but = findViewById(R.id.butOption4)


        //check for the final question

        if(currentquestion == Qdata.results.size - 1) {
            Sbut.text = "Finish"

        }





        //list of options that are not enabled with real values
        var listObut = mutableListOf<Button>(O1but,O2but,O3but,O4but)

        QTV.text = Qdata.results[currentquestion].question

        canspos = (1..4).random()


        when (canspos) {
            1 -> {
                O1but.text = Qdata.results[currentquestion].correct_answer
                listObut.remove(O1but)
            }
            2 -> {
                O2but.text = Qdata.results[currentquestion].correct_answer
                listObut.remove(O2but)
            }
            3 -> {
                O3but.text = Qdata.results[currentquestion].correct_answer
                listObut.remove(O3but)
            }
            4 -> {
                O4but.text = Qdata.results[currentquestion].correct_answer
                listObut.remove(O4but)
            }

        }

        var count = 1
        for (i in 0..2)   {
            listObut.get(i).text =  Qdata.results[currentquestion].incorrect_answers[i]


        }


        //adding onclick listeners
        O1but.setOnClickListener() {



            if (flag == false) {
                //condition for the correct answer
                if (canspos == 1) {
                    QDataSingleton.Companion.score  =   QDataSingleton.Companion.score + 1
                    O1but.setBackgroundColor(Color.GREEN)
                    O1but.setTextColor(Color.BLACK)


                } else {
                    O1but.setBackgroundColor(Color.RED)
                }
            }
            flag = true




        }
        //adding onclick listeners
        O2but.setOnClickListener() {

            if (flag == false) {
                //condition for the correct answer
                if (canspos == 2) {
                    QDataSingleton.Companion.score  =   QDataSingleton.Companion.score + 1
                    O2but.setBackgroundColor(Color.GREEN)
                    O2but.setTextColor(Color.BLACK)


                } else {
                    O2but.setBackgroundColor(Color.RED)
                }
            }
            flag = true

        }
        O3but.setOnClickListener() {
            if (flag == false) {
                //condition for the correct answer
                if (canspos == 3) {
                    QDataSingleton.Companion.score  =   QDataSingleton.Companion.score + 1
                    O3but.setBackgroundColor(Color.GREEN)
                    O3but.setTextColor(Color.BLACK)
                }else {
                    O3but.setBackgroundColor(Color.RED)
                }
            }
            flag = true




        }
        O4but.setOnClickListener() {
            if (flag == false) {
                //condition for the correct answer
                if (canspos == 4) {
                    QDataSingleton.Companion.score  =   QDataSingleton.Companion.score + 1
                    O4but.setBackgroundColor(Color.GREEN)
                    O4but.setTextColor(Color.BLACK)
                }else {
                    O4but.setBackgroundColor(Color.RED)
                }
            }
            flag = true




        }


        Sbut.setOnClickListener(){


            // if the currentquestion is final availabel questions go to score board
            if (currentquestion == Qdata.results.size -1 ) {
                val intent = Intent(this, Score::class.java).apply {
                    putExtra("score",  QDataSingleton.Companion.score)

                }
                startActivity(intent)
                finish()
            }

            // else show the current question to play


            val intent = Intent(this, MainActivity::class.java).apply {
                putExtra("currentQuestion", currentquestion+1)

            }
            startActivity(intent)
            finish()




        }























    }






}
