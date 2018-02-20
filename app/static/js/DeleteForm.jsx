import React from 'react';
import axios from 'axios';
import './css/loginform.css';
import { hashHistory } from 'react-router';

export default class DeleteForm extends React.Component {
   constructor(props) {
      super(props);
      
      this.state = {
         task_heading: "",
      }
      this.updateState = this.updateState.bind(this);
      this._onChange = this._onChange.bind(this);

   };
   updateState(e) {
      this.setState({task_heading: e.target.value});
   }
   _onChange(event) {
    event.preventDefault();
    axios.post("http://localhost:5000/dataDelete",{
        task_heading: this.state.task_heading
    }).then(function(response){
        console.log(response);
       console.log("Data submitted successfully");
       hashHistory.push('/HomePage');
    }).catch((error)=> {
          alert(error)
          console.log("got errr while posting data", error);
      });
  }
   render() {
      return (
        <div className="container">
          <div className="row">
            <div className="form_bg">
                <form>
                  <h2 className="text-center">Delete Task</h2>
                  <br/>
                  <div className="form-group">
                    <input type="text" className="form-control" id = "task_heading" 
                    name = "task_heading" value = {this.state.task_heading} 
                    onChange = {this.updateState} placeholder="Task Heading" />
                  </div>
                  <div className="align-center">
                    <button type="submit" className="btn btn-default" id="login" 
                    onClick={this._onChange}>Delete</button>
                  </div>
                </form>
            </div>
          </div>
        </div>
      );
   }
}
