import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { registerLicense } from '@syncfusion/ej2-base';
import { AppModule } from './app/app.module';

registerLicense('Ngo9BigBOggjHTQxAR8/V1NGaF1cXGFCf1FpRmJGdld5fUVHYVZUTXxaS00DNHVRdkdnWH9cdHZVRmRdVE1yWUI=');
platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));
