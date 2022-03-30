import "./index.css"
const Scorebaord=(props)=>{
    const{count}=props 
    const a=count<7 ? "spanE":"spanE1"
    return(
        <div className="score-main-container">
            <div className="score-container">
                <h1 className="score-head">Score is : <span className={a}>{count}</span></h1>
            </div>
        </div>
    )
}

export default Scorebaord;