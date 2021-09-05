import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { API_URL } from '../env';

@Injectable({
  providedIn: 'root',
})
export class FileUploadService {

  constructor(private http: HttpClient) { }

  downloadExcelPairings(formData: FormData): void {
    this.http.post(API_URL + '/pair', formData, { responseType: 'blob' })
      .subscribe(res => {
        console.log('in file upload service')
        console.log(res);

        // TODO: change this so a new tab doesn't need to open
        const blob = new Blob([res], { type: 'application/octet-stream' });
        const url = window.URL.createObjectURL(blob);
        window.open(url);
      })
  }

}