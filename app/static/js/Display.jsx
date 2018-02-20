import React from 'react';
import axios from 'axios';
import './css/loginform.css';
import { hashHistory } from 'react-router';
import ReactDOM from 'react-dom'

export default class Display extends React.Component {
   constructor(props) {
      super(props);
      this.state = {
      	res: []
      }
      // this.componentDidMount = this.componentDidMount.bind(this);
    }
    componentDidMount() {
  
    	axios.get("http://localhost:5000/dataDisplay").then(res => {    
    		
    		//this.state.res = result["json_list"]
    		//alert(res.data.json_list);
    		this.setState({res: res.data.json_list});
    	})
  	}
  	render() {
  		const JsonTable = require('ts-react-json-table')
		return (
			<div>
		 		<JsonTable rows = {this.state.res} />
		 	</div>
		 );
	}
}