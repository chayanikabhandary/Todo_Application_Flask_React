// App.jsx
import React from 'react';

class App extends React.Component {
   constructor(props) {
      super(props);
      
      this.state = {
         task_description: "",
         due_date: "",
         status: "",
         created_by: "",
         created_at: ""
      }
      this.updateState = this.updateState.bind(this);
   };
   updateState(e) {
      this.setState({task_description: e.target.value});
   }
   render() {
      return (
         <div>
         	<form method="POST" action= "" >
            Task Description: <input type = "text" value = {this.state.task_description} 
               onChange = {this.updateState} name = "task_description" />
            <br />
            Due date: <input type = "datetime-local" value = {this.state.due_date} 
               onChange = {this.updateState} name = "due_date" />
            <br />
            Status: <input type = "checkbox" value = {this.state.status} 
               onChange = {this.updateState} name = "status" />
            <br />
            Created By: <input type = "text" value = {this.state.created_by} 
               onChange = {this.updateState} name = "created_by" />
            <br />
            Created At: <input type = "datetime-local" value = {this.state.create_at} 
               onChange = {this.updateState} name = "created_at" />
            <br />

            <input type= "submit" onClick={this._onChange} value = "Done"/>


            </form>
         </div>
      );
   }

   _onChange(event) {
    axios.post("http://localhost:5000/test",{
        task_description: this.state.task_description,
        due_data: this.state.due_data,
        status: this.state.status,
        created_by: this.state.created_by,
        created_at: this.state.created_at
    }).then((response)=> {
       console.log("Data submitted successfully");
    }).catch((error)=> {
       		console.log("got errr while posting data", error);
    	});
	}

}
export default App;