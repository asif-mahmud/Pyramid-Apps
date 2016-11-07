/**
 * Created by shimon on 11/7/16.
 */
import {NgModule} from "@angular/core";
import {BrowserModule} from "@angular/platform-browser";
import {FormsModule} from "@angular/forms";
import {HttpModule, JsonpModule} from "@angular/http";
import {RegistrationForm} from "./reg.component";


@NgModule({
    imports:[BrowserModule, FormsModule, HttpModule, JsonpModule],
    declarations:[RegistrationForm],
    bootstrap:[RegistrationForm]
})
export class RegistrationModule{}
