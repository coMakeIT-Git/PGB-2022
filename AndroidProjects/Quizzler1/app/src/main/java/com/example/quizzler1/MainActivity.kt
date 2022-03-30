package com.example.quizzler1
import android.annotation.SuppressLint
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.Toast
import android.widget.EditText
import androidx.appcompat.widget.AppCompatButton
import androidx.appcompat.widget.AppCompatEditText
import com.google.android.material.textfield.TextInputEditText




class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)


        //ALways declare local vars in here  page consists two feilds

        var etName:AppCompatEditText=findViewById(R.id.etName)
        var btnStart:AppCompatButton=findViewById(R.id.btnStart)


        // Button Action using setOnclick
        btnStart.setOnClickListener {

            if (etName.text.toString().isEmpty()) {
                Toast.makeText(this, "Please Enter your Name", Toast.LENGTH_SHORT).show()
            } else {
                 intent = Intent(this, QuizQuestion::class.java)
                startActivity(intent)
               // System.out.println("hllo")
            }
        }

    }
}
