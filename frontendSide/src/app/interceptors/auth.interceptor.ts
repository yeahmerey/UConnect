import { Injectable } from "@angular/core";

import {
  HttpRequest , 
  HttpHandler , 
  HttpEvent , 
  HttpInterceptor 
} from '@angular/common/http'; 

import { Observable } from "rxjs";

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  constructor(){

  }
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const access = localStorage.getItem('access')
    if (access){
      
    }
    return next.handle(req)
  }
}