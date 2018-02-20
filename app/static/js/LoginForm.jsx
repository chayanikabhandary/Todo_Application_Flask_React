import React from 'react';
import axios from 'axios';
import './css/loginform.css';
import { hashHistory } from 'react-router';

export default class LoginForm extends React.Component {
   constructor(props) {
      super(props);
      
      this.state = {
         username: "",
         email: "",
         password: "",
         remember_me: "",
         
      }
      this.updateStateUsername = this.updateStateUsername.bind(this);
      this.updateStateEmail = this.updateStateEmail.bind(this);
      this.updateStatePassword = this.updateStatePassword.bind(this);
      this.updateStateRememberMe = this.updateStateRememberMe.bind(this);
      this._onChange = this._onChange.bind(this);

   };
   updateStateUsername(e) {
      this.setState({username: e.target.value});
   }
   updateStateEmail(e) {
      this.setState({email: e.target.value});
   }
   updateStatePassword(e) {
      this.setState({password: e.target.value});
   }
   updateStateRememberMe(e) {
      this.setState({remember_me: e.target.value});
   }
   _onChange(event) {
    event.preventDefault();
    axios.post("http://localhost:5000/login",{
        username: this.state.username,
        email: this.state.email,
        password: this.state.password,
        remember_me: this.state.remember_me
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
                  <h2 className="text-center">Login Page</h2>
                  <br/>
                  <div className="form-group">
                    <input type="text" className="form-control" id = "username" 
                    name = "username" value = {this.state.username} 
                    onChange = {this.updateStateUsername} placeholder="Username" required />
                  </div>
                  <div className="form-group">
                    <input type="email" className="form-control" id="email"
                    name="email" value = {this.state.email} 
                    onChange = {this.updateStateEmail} placeholder="Email id" required/>
                  </div>
                  <div className="form-group">
                    <input type="password" className="form-control" id="password"
                    name="password" value = {this.state.password} 
                    onChange = {this.updateStatePassword} placeholder="Password" required/>
                  </div>
                  <br/>
                    <input type="checkbox" className="form-control" id="remember_me"
                    name="remember_me" value = {this.state.remember_me} 
                    onChange = {this.updateStateRememberMe} /> Remember me?
                  
                  <div className="align-center">
                    <button type="submit" className="btn btn-default" id="login" 
                    onClick={this._onChange}>Login</button>
                  </div>
                </form>
            </div>
          </div>
        </div>
      );
   }
}
//export default App;