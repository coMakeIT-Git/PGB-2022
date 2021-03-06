const mongoose = require('mongoose')

const QuestionSchema = new mongoose.Schema({
    score:Number,
    category:String,
    level:String,
    description: String,
    correct_answer: String, 
    incorrect_answers: [
        {
            text: {
                type: String,
                required: true
            }
        }
    ]
})

module.exports = mongoose.model('Question', QuestionSchema)
