import {json_s} from "./display_priorities.js";
import http from 'http';
http.createServer(function(req,res){
    res.writeHead(200, {'Content-Type': 'application/json'});
    res.write(json_s);
    res.end();
}).listen(8000);