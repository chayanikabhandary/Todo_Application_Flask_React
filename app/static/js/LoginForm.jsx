import React from 'react';

class App extends React.Component {
   constructor(props) {
      super(props);
      
      this.state = {
         username: "",
         password: "",
         remember_me: "",
         
      }
      this.updateState = this.updateState.bind(this);
   };
   updateState(e) {
      this.setState({username: e.target.value});
   }
   render() {
      return (
         <div>
         	<form method="POST" action= "" >
            Username: <input type = "text" value = {this.state.username} 
               onChange = {this.updateState} name = "username" />
            <br />
            Password: <input type = "password" value = {this.state.password} 
               onChange = {this.updateState} name = "password" />
            <br />
            Remember me: <input type = "checkbox" value = {this.state.remember_me} 
               onChange = {this.updateState} name = "status" />
            <br />
            

            <input type= "submit" onClick={this._onChange} value = "Done"/>


            </form>
         </div>
      );
   }

   _onChange(event) {
    axios.post("http://localhost:5000/test",{
        username: this.state.username,
        password: this.state.password,
        remember_me: this.state.remember_me
    }).then((response)=> {
       console.log("Data submitted successfully");
    }).catch((error)=> {
       		console.log("got errr while posting data", error);
    	});
	}

}
export default App;