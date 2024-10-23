import { Component, ViewChild } from '@angular/core';
import { DocumentEditorContainerComponent } from '@syncfusion/ej2-angular-documenteditor';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'myangularproject';
  @ViewChild('documentEditor') editorObj !: DocumentEditorContainerComponent;

  public onSave(){
    this.editorObj.documentEditor.save('sampleDocument', 'Docx');
  }
}
