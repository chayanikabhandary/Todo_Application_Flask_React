import React from 'react'
import { Link } from 'react-router'
import './css/loginform.css';
import { hashHistory } from 'react-router';
  
export default class HomePage extends React.Component {
  // componentDidMount() {
  //   hashHistory.push('/');
  // }

  render() {
    return (
      <div>
        <h1>ToDo Application</h1>
        <ul role="nav">
          <li><Link to="/CreateForm">Create</Link></li>
          <li><Link to="/UpdateForm">Update</Link></li>
          <li><Link to="/DeleteForm">Delete</Link></li>
          <li><Link to="/Display">Display</Link></li>
          <li><a href="http://localhost:5000/logout">Logout</a></li>
        </ul>
      </div>
    )
  }
}