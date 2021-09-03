import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatToolbarModule} from "@angular/material/toolbar";
import { FileUploadComponent } from './file-upload/file-upload.component';
import {MatIconModule} from "@angular/material/icon";
import {HttpClientModule} from "@angular/common/http";
import { HeaderComponent } from './header/header.component';

@NgModule({
  declarations: [
    AppComponent,
    FileUploadComponent,
    HeaderComponent
  ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        BrowserAnimationsModule,
        MatToolbarModule,
        MatIconModule,
        HttpClientModule
    ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
