import React from 'react';
import axios from 'axios';
import './css/loginform.css';

export default class UpdateForm extends React.Component {
   constructor(props) {
      super(props);
      
      this.state = {
         task_heading: "",
         new_task_description: "",
         new_due_date: "",
         new_status: "",
         
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
      this.setState({new_task_description: e.target.value});
   }
   updateStateDueDate(e) {
      this.setState({new_due_date: e.target.value});
   }
   updateStateStatus(e) {
      this.setState({new_status: e.target.value});
   }
   _onChange(event) {
    event.preventDefault();
    axios.post("http://localhost:5000/dataUpdate",{
        task_heading: this.state.task_heading,
        new_task_description: this.state.new_task_description,
        new_due_date: this.state.new_due_date,
        new_status: this.state.new_status
    }).then(function(response){
       console.log("Data submitted successfully");
       hashHistory.push('/HomePage');
       
    }).catch((error)=> {
          console.log("got errr while posting data", error);
      });
  }
   render() {
      return (
        <div className="container">
          <div className="row">
            <div className="form_bg">
                <form>
                  <h2 className="text-center">Update Task</h2>
                  <br/>
                  <div className="form-group">
                    <input type="text" className="form-control" id = "task_heading" 
                    name = "task_heading" value = {this.state.task_heading} 
                    onChange = {this.updateStateTaskHeading} placeholder="Task Heading" />
                  </div>
                  <div className="form-group">
                    <input type="text" className="form-control" id="new_task_description"
                    name="new_task_description" value = {this.state.new_task_description} 
                    onChange = {this.updateStateTaskDescription} placeholder="New Task Description" />
                  </div>
                  <div className="form-group">
                    <input type="datetime-local" className="form-control" id="new_due_date"
                    name="new_due_date" value = {this.state.new_due_date} 
                    onChange = {this.updateStateDueDate} placeholder="New Due Date" />
                  </div>
                  <br/>
                    <input type="checkbox" className="form-control" id="new_status"
                    name="new_status" value = {this.state.new_status} 
                    onChange = {this.updateStateStatus} /> New Status?
                  
                  <div className="align-center">
                    <button type="submit" className="btn btn-default" id="update" 
                    onClick={this._onChange}>Update</button>
                  </div>
                </form>
            </div>
          </div>
        </div>
      );
   }

   

}
//export default App;