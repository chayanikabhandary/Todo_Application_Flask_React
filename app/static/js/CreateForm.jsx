import React from 'react';
import axios from 'axios';
import './css/loginform.css';
import { hashHistory } from 'react-router';

export default class CreateForm extends React.Component {
   constructor(props) {
      super(props);
      
      this.state = {
         task_heading: "",
         task_description: "",
         due_date: "",
         status: "",
         
      }
      this.updateStateTaskHeading = this.updateStateTaskHeading.bind(this);
      this.updateStateTaskDescription = this.updateStateTaskDescription.bind(this);
      this.updateStateDueDate = this.updateStateDueDate.bind(this);
      this.updateStateStatus = this.updateStateStatus.bind(this);
      this._onChange = this._onChange.bind(this);

   };
   updateStateTaskHeading(e) {
      this.setState({task_heading: e.target.value});
   }
   updateStateTaskDescription(e) {
      this.setState({task_description: e.target.value});
   }
   updateStateDueDate(e) {
      this.setState({due_date: e.target.value});
   }
   updateStateStatus(e) {
      this.setState({status: e.target.value});
   }
   _onChange(event) {
    event.preventDefault();
    axios.post("http://localhost:5000/dataPopulate",{
        task_heading: this.state.task_heading,
        task_description: this.state.task_description,
        due_date: this.state.due_date,
        status: this.state.status
    }).then((response)=> {
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
                  <h2 className="text-center">Create Task</h2>
                  <br/>
                  <div className="form-group">
                    <input type="text" className="form-control" id = "task_heading" 
                    name = "task_heading" value = {this.state.task_heading} 
                    onChange = {this.updateStateTaskHeading} placeholder="Task Heading" />
                  </div>
                  <div className="form-group">
                    <input type="text" className="form-control" id="task_description"
                    name="task_description" value = {this.state.task_description} 
                    onChange = {this.updateStateTaskDescription} placeholder="Task Description" />
                  </div>
                  <div className="form-group">
                    <input type="datetime" className="form-control" id="due_date"
                    name="due_date" value = {this.state.due_date} 
                    onChange = {this.updateStateDueDate} placeholder="Due Date" />
                  </div>
                  <br/>
                    <input type="checkbox" className="form-control" id="status"
                    name="status" value = {this.state.status} 
                    onChange = {this.updateStateStatus} /> Status?
                  
                  <div className="align-center">
                    <button type="submit" className="btn btn-default" id="create" 
                    onClick={this._onChange}>Create</button>
                  </div>
                </form>
            </div>
          </div>
        </div>
      );
   }

   

}
//export default App;