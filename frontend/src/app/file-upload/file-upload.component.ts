import { Component, OnInit } from '@angular/core';
import { HttpClient } from "@angular/common/http";

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

    // TODO: update URL
    // TODO: move this to a service
    this.http.post('url', formData)
      .subscribe(res => {
        console.log(res);
      })
  }

}
