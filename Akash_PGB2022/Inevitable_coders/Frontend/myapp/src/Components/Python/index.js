import {Component} from "react"
import QuestionItem from "../QuestionItem"
import Scorebaord  from "../Scoreboard";
import "./index.css";

class Python extends Component{

    state = { questionData: [], count:0, temp:{},isScoreOpen:false}

    componentDidMount(){
        this.getdata()
    }

    getdata=async()=>{
        const response=await fetch("http://localhost:5000/python")
        const data=await response.json()
        const sliceddata=data.slice(0,10)
        this.setState({  questionData:sliceddata})
    }
    
    formsubmit=(event)=>{
        const{temp}=this.state
        event.preventDefault()
        for (const key in temp) {
            if(key===temp[key]){
                this.setState(prevstate=>({count:prevstate.count+1}))
            }
        }
        this.setState({temp:" ",isScoreOpen:true})
    }

    changeradio=(event)=>{         
        this.state.temp[event.target.value] = event.target.id;
    }

    render(){
        const{questionData,count,isScoreOpen}=this.state;
        return(
            <div>
                {isScoreOpen?<Scorebaord count={count}/>:
                (<form className="python-container" onSubmit={this.formsubmit}>    
                    <h1 className="heading" align="center">Choose the correct Answers</h1>
                    {questionData.map(x=>(<QuestionItem questiondata={x} key={x.SNo} changeradio={this.changeradio}/>))}
                    <button type="submit" className="buttonE">Submit</button>
                </form>
                )}
            </div>
        )
       
    }
}

export default Python