import { Component, OnInit } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { API_URL } from '../env';

@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.scss']
})
export class FileUploadComponent implements OnInit {
  file: File | null = null;

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }

  onFileSelected(event: any) {
    console.log(event);
    this.file = <File>event.target.files[0];

    const formData = new FormData();
    formData.append('image', this.file, this.file.name);

    // TODO: move this to a service
    // TODO: change this so a new tab doesn't need to open
    this.http.post(API_URL + '/pair', formData, { responseType: 'blob' })
      .subscribe(res => {
        console.log(res);

        const blob = new Blob([res], { type: 'application/octet-stream' });
        const url = window.URL.createObjectURL(blob);
        window.open(url);
      })
  }

}
