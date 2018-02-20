import React from 'react';
import axios from 'axios';
import './css/loginform.css';
import { hashHistory } from 'react-router';

export default class RegisterForm extends React.Component {
   constructor(props) {
      super(props);
      
      this.state = {
         username: "",
         email: "",
         password: ""
      }
      this.updateStateUsername = this.updateStateUsername.bind(this);
      this.updateStateEmail = this.updateStateEmail.bind(this);
      this.updateStatePassword = this.updateStatePassword.bind(this);
      this._onChange = this._onChange.bind(this);

   };
   commonValidate() {
    //you could do something here that does general validation for any form field
    return true;
  }
   updateStateUsername(e) {
      this.setState({username: e.target.value});
   }
   updateStateEmail(e) {
      this.setState({email: e.target.value});
   }
   updateStatePassword(e) {
      this.setState({password: e.target.value});
   }
   _onChange(event) {
    event.preventDefault();
    axios.post("http://localhost:5000/register",{
        username: this.state.username,
        email: this.state.email,
        password: this.state.password
    }).then(function(response){
        console.log(response);
        console.log("Data submitted successfully");
       hashHistory.push('/');
    }).catch((error)=> {
          alert(error)
          
      });
  }
   render() {
      return (
        <div className="container">
          <div className="row">
            <div className="form_bg">
                <form>
                  <h2 className="text-center">Registration Page</h2>
                  <br/>
                  <div className="form-group">
                    <input type="text" className="form-control" id = "username" 
                    name = "username" value = {this.state.username} 
                    onChange = {this.updateStateUsername} validate = {this.commonValidate} placeholder="Username" />
                  </div>
                  <div className="form-group">
                    <input type="email" className="form-control" id="email"
                    name="email" value = {this.state.email} 
                    onChange = {this.updateStateEmail} placeholder="Email id" />
                  </div>
                  <div className="form-group">
                    <input type="password" className="form-control" id="password"
                    name="password" value = {this.state.password} 
                    onChange = {this.updateStatePassword} placeholder="Password" />
                  </div>
                  <br/>
                  <div className="align-center">
                    <button type="submit" className="btn btn-default" id="login" 
                    onClick={this._onChange}>Register</button>
                  </div>
                </form>
            </div>
          </div>
        </div>
      );
   }
}