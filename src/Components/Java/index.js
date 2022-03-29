import {Component} from "react"
//import QuestionItem from "../QuestionItem"
import "./index.css";

class Java extends Component{

    state = { questionData: [],currentindex:0, radioinput:"" , radioanswer:"", count:0}

    
    getdata=async()=>{
        const {currentindex}=this.state
        const response=await fetch("http://localhost:5000/java")
        const data=await response.json()
        const slicedata = data.slice(0,10);
        this.setState({  questionData: slicedata[currentindex]})
    }

    changeradio=(event)=>{
        this.setState({radioinput:event.target.id, radioanswer:event.target.value})      
    }
                   
    formsubmit=(event)=>{       
        event.preventDefault()       
    }

    nextquestion=()=>{
        const{radioanswer,radioinput}=this.state
        if(radioanswer===radioinput){
            this.setState(prevstate=> ({count:prevstate.count+1}))
        }
        this.setState(prevstate=>({currentindex:prevstate.currentindex+1}))
    }

    renderquestions=()=>{
        this.getdata()
        const{questionData,currentindex}=this.state;
        const{SNo,Question,Option1,Option2,Option3,Option4,Answer}=questionData
        return(
            <div className="java-container" >                   
                    <h1 className="heading" align="center">Choose the correct Answers</h1>               
                    <div className="item-container">
                        <h1 className="item-head">{SNo}.{Question}</h1>
                        <div className="option-container" onChange={this.changeradio} >
                            <label><input type="radio" id={Option1} value={Answer} name={SNo} className="inputE" />{Option1}</label>
                            <label><input type="radio"  id={Option2}  value={Answer} name={SNo} className="inputE"/>{Option2}</label>
                            <label><input type="radio"  id={Option3}  value={Answer} name={SNo} className="inputE"/>{Option3}</label>
                            <label><input type="radio"  id={Option4} value={Answer}  name={SNo} className="inputE"/>{Option4}</label>
                        </div>
                    </div>  
                    {currentindex<9?<button type="button" className="buttonE" onClick={this.nextquestion}>Next</button>:<button type="submit" onSubmit={this.formsubmit} className="buttonE">Submit</button>}               
            </div>
        )
    }
    render(){
        return this.renderquestions()
    }
}

export default Java;
