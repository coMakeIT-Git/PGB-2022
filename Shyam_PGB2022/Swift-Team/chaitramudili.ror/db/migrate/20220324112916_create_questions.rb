class CreateQuestions < ActiveRecord::Migration[6.1]
  def change
    create_table :questions do |t|
      t.string :category
      t.string :difficulty
      t.string :questionString
      t.string :correct_answer
      t.string :incorrect_answers, array: true

      t.timestamps
    end
  end
end
