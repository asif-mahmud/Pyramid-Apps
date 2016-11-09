/**
 * Created by shimon on 11/8/16.
 */
import {platformBrowserDynamic} from "@angular/platform-browser-dynamic";
import {PetCollectionApp} from "./module";

let platform = platformBrowserDynamic();
platform.bootstrapModule(PetCollectionApp);
