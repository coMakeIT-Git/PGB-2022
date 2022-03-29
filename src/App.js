import './App.css';
import Home from "./Components/Home"
import Java from "./Components/Java"
import Python from "./Components/Python"
import JavaScript from "./Components/JavaScript"
import {BrowserRouter,Switch,Route} from "react-router-dom"
function App() {
  return (
    <>
      <BrowserRouter>
        <Switch>
          <Route path="/Java" component={Java}/>
          <Route path="/Python" component={Python}/>
          <Route path="/JavaScript" component={JavaScript}/>
          <Route exact path="/" component={Home}/>
        </Switch>
      </BrowserRouter>
    </>
  );
}

export default App;
