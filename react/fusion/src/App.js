import React from 'react';
import DocViewer from 'react-doc-viewer';

const DocumentEmbed = () => {
  const documents = [
    {
      uri: './Juan.docx', // The path to your Word document
      fileType: 'docx',
    },
  ];

  return (
    <div>
      <DocViewer documents={documents} />
    </div>
  );
};

export default DocumentEmbed;

