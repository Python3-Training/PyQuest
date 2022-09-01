/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.soft9000.qna1;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.soft9000.EnDecode.OctalExchange;

/**
 *
 * @author profnagy
 */
public class BasicQuestion {

    static BasicQuestion FromClipboard(String data) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    static String Encode(String str) {
        OctalExchange oder = new OctalExchange();
        return oder.encode(str);
    }

    static String Decode(String str) {
        OctalExchange oder = new OctalExchange();
        return oder.decode(str);
    }

    public int id = 0;
    public String KID = "";
    public String GID = "";
    public String Difficulty = "";
    public String Association = "";
    public String Status = "";
    public String Question = "";
    public String Answer = "";

    @Override
    public boolean equals(Object obj) {
        if (obj == null || (obj instanceof BasicQuestion) == false) {
            return false;
        }
        BasicQuestion inst = (BasicQuestion) obj;
        if (inst.id != this.id) {
            return false;
        }
        if (inst.GID.equals(this.GID)) {
            return false;
        }
        if (inst.KID.equals(this.KID)) {
            return false;
        }
        if (inst.Status.equals(this.Status)) {
            return false;
        }
        if (inst.Difficulty.equals(this.Difficulty)) {
            return false;
        }
        if (inst.Association.equals(this.Association)) {
            return false;
        }
        if (inst.Question.equals(this.Question)) {
            return false;
        }
        if (inst.Answer.equals(this.Answer)) {
            return false;
        }
        return true;
    }

    /**
     * Opportunity to see an editable template (etc) whilst we are using the
     * JSON format.
     *
     * @return
     */
    public static String GetNewJSON() {
        return BasicQuestion.ToJSON(new BasicQuestion());
    }

    /**
     * Create an object from a JSON / user edited string.
     *
     * @param prop Data to parse.
     * @return Object parsed, else null.
     */
    public static BasicQuestion FromJSON(String prop) {
        try {
            Gson gson = new Gson();
            return gson.fromJson(prop, BasicQuestion.class);
        } catch (Exception ex) {
        }
        return null;
    }

    /**
     * Extract a JSON string from an object.
     *
     * @param bq
     * @return Object data, else a default / all empty JSON schema, for same.
     */
    public static String ToJSON(BasicQuestion bq) {
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        return gson.toJson(bq);
    }

    /**
     * The JSON parser is from Google - I have tested this version a lot.
     *
     * @param args
     */
    public static void main(String[] args) {
        BasicQuestion q1 = new BasicQuestion();
        BasicQuestion q2 = new BasicQuestion();
        assert (q1.equals(q2));
        q1.id = 6;
        assert (!q1.equals(q2));
        String d1 = BasicQuestion.ToJSON(q1);
        q2 = BasicQuestion.FromJSON(d1);
        assert (q1.equals(q2));
        System.out.println(d1);
        System.out.println("Testing Success.");
    }
}
