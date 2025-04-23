import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Profile } from '../models';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {

  private apiUrl = 'http://127.0.0.1:8000/api'; // Замените, если нужно

  constructor(private http: HttpClient) {}

  // Получаем профиль пользователя по имени пользователя
  getProfileByUsername(username: string): Observable<Profile> {
    return this.http.get<Profile>(`${this.apiUrl}/profile/${username}/`);
  }
}
