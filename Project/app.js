import { router } from "./routes/priorities.js";
import express from 'express';

const app = express();

app.use("/", router);

export {app};