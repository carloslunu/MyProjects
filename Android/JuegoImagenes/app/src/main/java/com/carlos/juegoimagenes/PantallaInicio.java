package com.carlos.juegoimagenes;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class PantallaInicio extends AppCompatActivity {
    private EditText introducirnombre;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        introducirnombre = findViewById(R.id.introducirnom);
    }

    public void jugar(View view) {
        Intent i = new Intent(this, PantallaJuego.class);
        if (!TextUtils.isEmpty(introducirnombre.getText()) || introducirnombre== null) {
            String user = introducirnombre.getText().toString();
            i.putExtra("NOMBRE", user);
            introducirnombre.setText("");
            startActivity(i);
        } else {
            Toast.makeText(this, this.getString(R.string.ponelnombre), Toast.LENGTH_LONG).show();

        }


    }
}