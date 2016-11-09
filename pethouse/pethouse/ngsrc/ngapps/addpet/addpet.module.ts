/**
 * Created by shimon on 11/8/16.
 */
import {NgModule} from "@angular/core";
import {BrowserModule} from "@angular/platform-browser";
import {FormsModule} from "@angular/forms";
import {HttpModule, JsonpModule} from "@angular/http";
import {InitializeDropdown} from "../common/initui";
import {AddPetFormComponent} from "./addpet.component";
import {PetTypeService} from "../common/pettypes.service";
import {AddPetService} from "../common/addpet.service";


@NgModule({
    imports:[BrowserModule, FormsModule, HttpModule, JsonpModule],
    declarations:[InitializeDropdown, AddPetFormComponent],
    providers:[PetTypeService, AddPetService],
    bootstrap:[AddPetFormComponent]
})
export class AddPetModule{}
