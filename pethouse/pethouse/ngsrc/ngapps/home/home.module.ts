/**
 * Created by shimon on 11/3/16.
 */

import {NgModule} from "@angular/core";
import {BrowserModule} from "@angular/platform-browser";
import {FormsModule} from "@angular/forms";
import {HomePageComponent} from "./home.component";
import {HomeRegistrationForm} from "./home.registration.component";
import {HomeLoginComponent} from "./home.login.component";


@NgModule({
    imports:[BrowserModule, FormsModule],
    declarations:[HomePageComponent, HomeRegistrationForm, HomeLoginComponent],
    bootstrap:[HomePageComponent]
})
export class HomePageModule{}
