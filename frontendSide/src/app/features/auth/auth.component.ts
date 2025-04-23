import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthModel } from '../../core/models';
import { PostsService } from '../../core/services/posts.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-auth',
  imports: [CommonModule, FormsModule],
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css']
})
export class AuthComponent {
  authModel: AuthModel;

  constructor(private postService: PostsService, private router: Router) {
    this.authModel = {} as AuthModel;
  }

  login() {
    this.postService.login(this.authModel).subscribe(
      (token) => {
        localStorage.setItem('access', token.access);
        localStorage.setItem('refresh', token.refresh);
        localStorage.setItem('username', this.authModel.username);
  
        // Навигация на главную и обновление страницы
        this.router.navigate(['/']).then(() => window.location.reload());
      },
      (error) => {
        console.error('Ошибка входа:', error);
      }
    );
  }
  
}
