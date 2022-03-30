package com.example.Quizzler

import com.example.quizzler.QList
import retrofit2.Call
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.GET
import java.util.*

interface QuestionApi {

        @GET("/api.php?amount=10&category=18&difficulty=easy&type=multiple")
        fun getQuestions() : Call<QList>

        companion object RetrofitHelper {

                val baseUrl = "https://opentdb.com/"

                fun getInstance(): QuestionApi {
                        return Retrofit.Builder().baseUrl(baseUrl)
                                .addConverterFactory(GsonConverterFactory.create())
                                .build().create(QuestionApi::class.java)
                }
        }

}