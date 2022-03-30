package com.example.Quizzler

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.example.Quizzler.R
import com.example.quizzler.QList
import com.google.android.material.button.MaterialButton
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class Home : AppCompatActivity() {

    //declare global variables as lateinit to avoid compilation error
    lateinit  var Qdata : QList
    lateinit var Java : MaterialButton
    lateinit var Python : MaterialButton

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_home)


        val apiInterface = QuestionApi.getInstance().getQuestions()


        apiInterface.enqueue( object : Callback<QList> {
            override fun onResponse(call: Call<QList>?, response: Response<QList>?) {

                if (response?.body() != null) {
                    // System.out.println("-------------------------------" + response.body()!!)
                    Qdata = response.body() as QList  // type  casting to Qlist
                    printQuestion()
                }
            }
            override fun onFailure(call: Call<QList>?, t: Throwable?) {
                System.out.print("Failed to retro-----------------")

            }
        })


        Java = findViewById(R.id.javabut)
        Python = findViewById(R.id.pybut)



        Java.setOnClickListener() {




            QDataSingleton.Companion.QData = Qdata  // a common data source for entire app // initialisation
                                //source -> destination
            val intent = Intent(this, MainActivity::class.java).apply {
                putExtra("currentQuestion", 0)

            }
            startActivity(intent)




        }





        Python.setOnClickListener() {

            //QDataSingleton.Companion.score +=1


            Toast.makeText(this@Home, "score : " +  QDataSingleton.Companion.score.toString(), Toast.LENGTH_SHORT).show()
        }


    }

    fun printQuestion() {
        System.out.println( Qdata.results)
    }


}