import { provideHttpClient, HttpClient } from '@angular/common/http';
import {bootstrapApplication } from '@angular/platform-browser';
import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';



//loading = true; error = '';

//http.get<User[]>('/api/users').subcribe({
//  next: d => { users = d; loading = false; },
 // error: () => {error = 'Failed to load'; loading = false; }
//});

@Component({
    selector: 'app-root',
    standalone: true,
    imports: [CommonModule],
    template: `
      <h3> HttpClient</h3>
      <button (click)="load()">Load Priorities</button>
      <p *ngIf="loading">loading...</p>
      <p *ngIf="error" style="color:crimson">{{ error }}</p>
      <ul>
        <li *ngFor="let p of priorities">{{ p.title }} ({{ p.category }})</li>
      </ul>
    `
})

export class App {
  http = inject(HttpClient);
  priorities: any[] = [];
  loading = false;
  error = '';

  load() {
    this.loading = true;
    this.error = '';
    this.http.get<any[]>('http://localhost:8000')
      .subscribe({
        next:(data) => {this.priorities = data; this.loading = false; },
        error: () => { this.error = 'Failed to load correct data'; this.loading = false; }
      });
  }

}
 

bootstrapApplication(App, {providers: [provideHttpClient()]} );