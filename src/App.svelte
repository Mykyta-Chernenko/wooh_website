<script>
    import {Route, Router} from "svelte-routing";
    import Home from "./routes/Home.svelte";
    import Register from "./routes/Register.svelte";
</script>

<Router>
    <Route path="/register" component={Register}/>
    <Route path="/" component={Home}/>
    <Route path="/:inviteCode" let:params>
        <Home inviteCode={params.inviteCode}/>
    </Route>
</Router>
