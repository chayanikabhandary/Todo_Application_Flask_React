import React from 'react'
import './css/loginform.css';
import { Link } from 'react-router'
import { hashHistory } from 'react-router';
  
export default class LandingPage extends React.Component {
  componentDidMount() {
    hashHistory.push('/');
  }

  render() {
    return (
      <div>
        <h1>ToDo Application</h1>
        <ul role="nav">
          <li><Link to="/LoginForm">Login</Link></li>
          <li><Link to="/RegisterForm">Register</Link></li>

        </ul>
        {this.props.children}
      </div>
    )
  }
}