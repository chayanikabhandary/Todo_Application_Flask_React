import React from 'react'
import { Link } from 'react-router'
import { browserHistory } from 'react-router';
  
export default class App extends React.Component {
  componentDidMount() {
    browserHistory.push('/');
  }

  render() {
    return (
      <div>
        <h1>React Router</h1>
        <ul role="nav">
          <li><Link to="/LoginForm">Login</Link></li>
          
        </ul>
        {this.props.children}
      </div>
    )
  }
}