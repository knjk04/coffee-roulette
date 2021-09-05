import { Component, OnInit } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { API_URL } from '../env';
import { FileUploadService } from './file-upload.service';

@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.scss']
})
export class FileUploadComponent implements OnInit {
  file: File | null = null;

  constructor(private fileUploadService: FileUploadService) { }

  ngOnInit(): void {
  }

  onFileSelected(event: any) {
    this.file = <File>event.target.files[0];

    const formData = new FormData();
    formData.append('image', this.file, this.file.name);

    this.fileUploadService.downloadExcelPairings(formData);
  }
}
