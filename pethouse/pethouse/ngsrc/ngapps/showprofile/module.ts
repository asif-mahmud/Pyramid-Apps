/**
 * Created by shimon on 11/9/16.
 */
import {BrowserModule} from "@angular/platform-browser";
import {NgModule} from "@angular/core";
import {HttpModule, JsonpModule} from "@angular/http";
import {FormsModule} from "@angular/forms";
import {InitializeDropdown} from "common/initui";
import {PetCollectionComponent} from "../showpets/component";
import {AddPetFormComponent} from "../addpet/addpet.component";
import {AddPetService} from "common/addpet.service";
import {PetTypeService} from "common/pettypes.service";


@NgModule({
    imports:[BrowserModule, HttpModule, JsonpModule, FormsModule],
    declarations:[PetCollectionComponent, AddPetFormComponent, InitializeDropdown],
    bootstrap:[PetCollectionComponent, AddPetFormComponent],
    providers:[AddPetService, PetTypeService]
})
export class ShowProfileApp{}
