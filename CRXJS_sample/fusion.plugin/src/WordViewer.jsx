import React, { useRef, useEffect } from 'react';
import WebViewer from '@pdftron/webviewer'; // Make sure to have WebViewer installed

const WordViewer = () => {
  const viewer = useRef(null); // Create a reference for the WebViewer container

  useEffect(() => {
    WebViewer(
      {
        path: '/webviewer/lib', // Path to the WebViewer library files
        initialDoc: chrome.runtime.getURL('files/Juan.docx'), // Initial Word document to load
        enableOfficeEditing: true, // Enable Office document editing
      },
      viewer.current, // The container where WebViewer will be mounted
    ).then((instance) => {
      const { documentViewer, annotationManager, Annotations } = instance.Core;
      // Additional setup or handling can be done here
    }).catch((error) => {
      console.error("Error initializing WebViewer", error);
    });
  }, []);

  return (
    <div style={{ height: '100vh', width: '100%' }}>
      {/* The div where WebViewer will be mounted */}
      <div ref={viewer} style={{ height: '100%', width: '100%' }}></div>
    </div>
  );
};

export default WordViewer;
