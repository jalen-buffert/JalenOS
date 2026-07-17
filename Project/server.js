import {json_s} from "./display_priorities.js";
import http from 'http';
http.createServer(function(req,res){
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.writeHead(200, {'Content-Type': 'application/json'});
    //res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    //res.setHeader('Acces-Control-Allow-Headers', 'Content-Type');
    res.write(json_s);
    res.end();
}).listen(8000);