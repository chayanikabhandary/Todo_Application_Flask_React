import React from 'react';
import axios from 'axios';
import './css/loginform.css';

export default class LoginForm extends React.Component {
   constructor(props) {
      super(props);
      
      this.state = {
         username: "",
         password: "",
         remember_me: "",
         
      }
      this.updateState = this.updateState.bind(this);
      this._onChange = this._onChange.bind(this);

   };
   updateState(e) {
      this.setState({username: e.target.value});
   }
   _onChange(event) {
    axios.post("http://localhost:5000/test",{
        username: this.state.username,
        email: this.state.email,
        password: this.state.password
    }).then((response)=> {
       console.log("Data submitted successfully");
    }).catch((error)=> {
          console.log("got errr while posting data", error);
      });
  }
   render() {
      return (
        <div class="container">
          <div class="row">
            <div class="form_bg">
                <form>
                  <h2 class="text-center">Login Page</h2>
                  <br/>
                  <div class="form-group">
                    <input type="text" class="form-control" id = "username" 
                    name = "username" value = {this.state.username} 
                    onChange = {this.updateState} placeholder="Username" />
                  </div>
                  <div class="form-group">
                    <input type="email" class="form-control" id="email"
                    name="email" value = {this.state.password} 
                    onChange = {this.updateState} placeholder="Email id" />
                  </div>
                  <div class="form-group">
                    <input type="password" class="form-control" id="password"
                    name="password" value = {this.state.password} 
                    onChange = {this.updateState} placeholder="Password" />
                  </div>
                  <br/>
                  <div class="align-center">
                    <button type="submit" class="btn btn-default" id="login" onClick={this._onChange}>Login</button>
                  </div>
                </form>
            </div>
          </div>
        </div>
      );
   }

   

}
//export default App;