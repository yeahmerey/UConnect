import { Component, NgModule } from '@angular/core';
import { NgForm } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  imports: [CommonModule, FormsModule],
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  username = '';
  email = '';
  password = '';

  constructor(private http: HttpClient, private router: Router) {}

  register(form: NgForm) {
    if (form.valid) {
      const body = {
        username: this.username,
        email: this.email,
        password: this.password
      };
  
      this.http.post<any>('http://127.0.0.1:8000/api/auth/register/', body)
        .subscribe({
          next: (res) => {
            // Сохраняем токены
            localStorage.setItem('access', res.access);
            localStorage.setItem('refresh', res.refresh);
            localStorage.setItem('username', res.user.username);
  
            // Перенаправление на главную
            this.router.navigate(['/']);
          },
          error: err => {
            alert('Ошибка регистрации: ' + (err.error.detail || JSON.stringify(err.error)));
          }
        });
    }
  }
}
