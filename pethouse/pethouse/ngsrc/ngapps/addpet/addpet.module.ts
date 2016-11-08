/**
 * Created by shimon on 11/8/16.
 */
import {NgModule} from "@angular/core";
import {BrowserModule} from "@angular/platform-browser";
import {FormsModule} from "@angular/forms";
import {HttpModule, JsonpModule} from "@angular/http";
import {InitializeDropdown} from "common/initui";
import {AddPetFormComponent} from "./addpet.component";


@NgModule({
    imports:[BrowserModule, FormsModule, HttpModule, JsonpModule],
    declarations:[InitializeDropdown, AddPetFormComponent],
    bootstrap:[AddPetFormComponent]
})
export class AddPetModule{}
