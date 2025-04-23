import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-navbar',
  imports: [CommonModule, RouterModule], 
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  username: string | null = null;

  ngOnInit(): void {
    // Получаем имя пользователя из localStorage, если оно там есть
    this.username = localStorage.getItem('username');
  }

  logout() {
    // Очистить токены и данные пользователя из localStorage
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    localStorage.removeItem('username');
    

    // Перенаправление на страницу входа после выхода
    window.location.href = '/auth';  // Можете использовать Router для навигации
  }
}
